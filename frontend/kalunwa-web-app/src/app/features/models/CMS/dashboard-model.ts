export interface DashboardModel{
  id: number;
  website_views: number;
  pages: number;
  administrators: number;
  newsletter_subs: number;
  applicants: number;
  audit_logs: Array<any>;
}
