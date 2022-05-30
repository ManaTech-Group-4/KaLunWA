import { Component, OnInit } from '@angular/core';
import { DashboardModel } from 'src/app/features/models/CMS/dashboard-model';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  dashboard: DashboardModel={
    id: 1,
    website_views: 1081,
    pages: 18,
    administrators: 6,
    newsletter_subs: 24,
    audit_logs: [
      {
        id: 1,
        administrator: "Name1",
        content_changed: "Homepage-content",
        action: "add something",
        date: "06/08/2021",
        time: "12:51 AM"
      },
      {
        id: 2,
        administrator: "Name2",
        content_changed: "Events-content",
        action: "edit something",
        date: "04/12/2022",
        time: "03:15 PM"
      },
      {
        id: 3,
        administrator: "Name3",
        content_changed: "Projects-content",
        action: "delete something",
        date: "11/21/2021",
        time: "06:25 AM"
      },
      {
        id: 2,
        administrator: "Name2",
        content_changed: "Events-content",
        action: "edit something",
        date: "04/12/2022",
        time: "03:15 PM"
      },
      {
        id: 3,
        administrator: "Name3",
        content_changed: "Projects-content",
        action: "delete something",
        date: "11/21/2021",
        time: "06:25 AM"
      },
    ],
  }

  constructor() { }

  ngOnInit(): void {
    
  }

}
