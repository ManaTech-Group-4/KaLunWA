import { AuditLogsModel } from "./audit-logs-model";

export interface DashboardModel{
  id: number;
  website_views: number;
  pages: number;
  administrators: number;
  newsletter_subs: number;
  audit_logs: Array<AuditLogsModel>;
}
