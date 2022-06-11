import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Admin, Profile, ProfileReceive } from 'src/app/admin/model/user-model';
import { AuthService } from 'src/app/admin/service/auth.service';
import { AdminListModel } from 'src/app/features/models/CMS/admin-list-model';

@Component({
  selector: 'app-admin-list',
  templateUrl: './admin-list.component.html',
  styleUrls: ['./admin-list.component.scss']
})
export class AdminListComponent implements OnInit {

  admin_list: ProfileReceive[] = [];
  is_superadmin: boolean;

  selectedAdmin:ProfileReceive;

  constructor(private ref: ChangeDetectorRef, private service: AuthService) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 5;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
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
  }

  ngOnInit(): void {
    this.service.getUsers().subscribe(
      data => {this.admin_list = data;
              this.selectedAdmin  = this.admin_list[0];
            }
    )
    this.is_superadmin = this.service.currentAdmin.is_superadmin;
  }

  displayInfo(admin:ProfileReceive){
    this.selectedAdmin = admin;
  }

}
