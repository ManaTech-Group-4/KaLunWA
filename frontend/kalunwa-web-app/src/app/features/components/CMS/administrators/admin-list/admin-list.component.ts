import { Component, OnInit } from '@angular/core';
import { AdminListModel } from 'src/app/features/models/CMS/admin-list-model';

@Component({
  selector: 'app-admin-list',
  templateUrl: './admin-list.component.html',
  styleUrls: ['./admin-list.component.scss']
})
export class AdminListComponent implements OnInit {

  admin_list: AdminListModel[] = [
    {
      id:1,
      admin_name: "Admin_1",
      username: "admin_1",
      first_name: "Jose",
      last_name: "Rizal",
      email: "j.riz@gmail.com",
      role: "Super Admin",
      date_added: "12/30/21",
    },
    {
      id:2,
      admin_name: "Admin_2",
      username: "admin_2",
      first_name: "Juan",
      last_name: "Dela Cruz",
      email: "jdcruz@gmail.com",
      role: "Admin",
      date_added: "04/05/21",
    },
    {
      id:3,
      admin_name: "Admin_3",
      username: "admin_3",
      first_name: "Joferlyn",
      last_name: "Robredo",
      email: "doc.joferlyn@gmail.com",
      role: "Admin",
      date_added: "09/12/21",
    },
  ]

  constructor() { }

  ngOnInit(): void {
  }

}
