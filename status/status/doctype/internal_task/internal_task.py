import frappe
from frappe.model.document import Document
from datetime import timedelta
from frappe.utils import get_datetime, getdate, today


class InternalTask(Document):

    def validate(self):
        self.set_sla_due_date()
        self.calculate_worklog_duration()
        self.calculate_total_effort()
        self.prevent_completion_without_logs()
        self.prevent_core_edit_after_approval()
        self.check_maker_checker()
    
    def before_save(self):
        self.set_sla_breach()


    # 1️⃣ SLA calculation
    def set_sla_due_date(self):
        if self.priority and not self.sla_due_date:
            base_date = getdate(self.sla_start_date) if self.sla_start_date else getdate(today())

            if self.priority == "Critical":
                self.sla_due_date = base_date
            elif self.priority == "High":
                self.sla_due_date = base_date + timedelta(days=1)
            elif self.priority == "Medium":
                self.sla_due_date = base_date + timedelta(days=3)
            elif self.priority == "Low":
                self.sla_due_date = base_date + timedelta(days=5)

    # 2️⃣ Work log duration per row
    def calculate_worklog_duration(self):
        for row in self.work_logs:
            if row.start_time and row.end_time:
                start = get_datetime(row.start_time)
                end = get_datetime(row.end_time)

                duration = (end - start).total_seconds() / 3600
                row.duration = round(duration, 2)

    # 3️⃣ Total effort sum
    def calculate_total_effort(self):
        self.total_effort = sum((row.duration or 0) for row in self.work_logs)

    # 4️⃣ Prevent completion without logs
    def prevent_completion_without_logs(self):
        if self.status == "Completed" and not self.work_logs:
            frappe.throw("Cannot complete task without work logs")

    # 5️⃣ Prevent core edit after approval
    def prevent_core_edit_after_approval(self):
        if not self.is_new():
            old = frappe.get_doc(self.doctype, self.name)

            if old.status in ["Approved", "In Execution", "Completed", "Closed"]:
                core_fields = [
                    "task_title",
                    "task_category",
                    "priority",
                    "requested_by",
                    "department"
                ]

                for field in core_fields:
                    if old.get(field) != self.get(field):
                        frappe.throw("Core fields cannot be changed after approval")

    # 6️⃣ Maker-Checker rule
    def check_maker_checker(self):
        if self.status == "Approved" and self.requested_by:
            requester_user = frappe.db.get_value("Employee", self.requested_by, "user_id")
            if requester_user == frappe.session.user:
                frappe.throw("Maker cannot approve their own task")

    # 7️⃣ SLA Breach flag
    def set_sla_breach(self):
        self.sla_breached = 0  # default reset

        if self.sla_due_date and self.status not in ["Completed", "Closed"]:
            if getdate(today()) > getdate(self.sla_due_date):
                self.sla_breached = 1
