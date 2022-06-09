import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
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
      picture: "assets/images/person-icon.jpg",
      username: "admin_1",
      first_name: "Jose",
      last_name: "Rizal",
      email: "j.riz@gmail.com",
      role: "Super Admin",
      date_added: "12/30/21",
    },
    {
      id:2,
      picture: "assets/images/person-icon.jpg",
      username: "admin_2",
      first_name: "Juan",
      last_name: "Dela Cruz",
      email: "jdcruz@gmail.com",
      role: "Admin",
      date_added: "04/05/21",
    },
    {
      id:3,
      picture: "assets/images/person-icon.jpg",
      username: "admin_3",
      first_name: "Joferlyn",
      last_name: "Robs",
      email: "doc.joferlyn@gmail.com",
      role: "Admin",
      date_added: "09/12/21",
    },
    {
      id:1,
      picture: "assets/images/person-icon.jpg",
      username: "admin_1",
      first_name: "Jose",
      last_name: "Rizal",
      email: "j.riz@gmail.com",
      role: "Super Admin",
      date_added: "12/30/21",
    },
    {
      id:2,
      picture: "assets/images/person-icon.jpg",
      username: "admin_2",
      first_name: "Juan",
      last_name: "Dela Cruz",
      email: "jdcruz@gmail.com",
      role: "Admin",
      date_added: "04/05/21",
    },
    {
      id:3,
      picture: "assets/images/person-icon.jpg",
      username: "admin_3",
      first_name: "Joferlyn",
      last_name: "Robs",
      email: "doc.joferlyn@gmail.com",
      role: "Admin",
      date_added: "09/12/21",
    },
    {
      id:1,
      picture: "assets/images/person-icon.jpg",
      username: "admin_1",
      first_name: "Jose",
      last_name: "Rizal",
      email: "j.riz@gmail.com",
      role: "Super Admin",
      date_added: "12/30/21",
    },
    {
      id:2,
      picture: "assets/images/person-icon.jpg",
      username: "admin_2",
      first_name: "Juan",
      last_name: "Dela Cruz",
      email: "jdcruz@gmail.com",
      role: "Admin",
      date_added: "04/05/21",
    },
    {
      id:3,
      picture: "assets/images/person-icon.jpg",
      username: "admin_3",
      first_name: "Joferlyn",
      last_name: "Robs",
      email: "doc.joferlyn@gmail.com",
      role: "Admin",
      date_added: "09/12/21",
    },
    {
      id:1,
      picture: "assets/images/person-icon.jpg",
      username: "admin_1",
      first_name: "Jose",
      last_name: "Rizal",
      email: "j.riz@gmail.com",
      role: "Super Admin",
      date_added: "12/30/21",
    },
  ]
  
  selectedAdmin?:AdminListModel = this.admin_list[0];

  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 5;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    console.log(newPage,this.activePage);
    this.currentPage += (6*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 6;
    if(this.lastPage > this.admin_list.length)
      this.lastPage = this.admin_list.length;

    this.ref.detectChanges();
    this.activePage = newPage;
    let y =  document.querySelector('.table-content')?.getBoundingClientRect().top;
    window.scrollTo({top: y! + window.scrollY - 80, behavior: 'smooth'});
    console.log(this.currentPage, this.lastPage);
  }

  ngOnInit(): void {
  }

  displayInfo(admin:AdminListModel){
    this.selectedAdmin = admin;
  }

}
