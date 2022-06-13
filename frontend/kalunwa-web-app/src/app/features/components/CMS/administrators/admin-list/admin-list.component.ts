import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ConfirmDialog } from 'src/app/admin/dialogs/confirm-dialog/confirm-dialog';
import { Admin, Profile, ProfileReceive } from 'src/app/admin/model/user-model';
import { AuthService } from 'src/app/admin/service/auth.service';

@Component({
  selector: 'app-admin-list',
  templateUrl: './admin-list.component.html',
  styleUrls: ['./admin-list.component.scss']
})
export class AdminListComponent implements OnInit {

  admin_list: ProfileReceive[] = [];
  is_superadmin: boolean;
  adminId:number;

  selectedAdmin:ProfileReceive;

  constructor(private ref: ChangeDetectorRef,
    private service: AuthService,
    private dialog: MatDialog) { }

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
    this.getList();
    const currentAdminSub = this.service.currentAdmin.subscribe(
      (res: ProfileReceive)=>{
        this.adminId = res.id;
        this.is_superadmin = res.is_superadmin;
        currentAdminSub.unsubscribe();
      }
    );
  }

  getList(){
    this.service.getUsers().subscribe(
      data => {this.admin_list = data;
              this.selectedAdmin  = this.admin_list[0];
            }
    )
  }

  displayInfo(admin:ProfileReceive){
    this.selectedAdmin = admin;
  }


  deleteUser(id:number, name: string){

    const dialogRef = this.dialog.open(ConfirmDialog, {
      width: '250px',
      data: `Do you like to delete the admin ${name}`,
    });

    const dialogSubscribe = dialogRef.afterClosed().subscribe(result => {
      if(result){
        const deleteSub = this.service.delete(id).subscribe(
          () => {
            console.log('success');
            this.getList();
            this.updateDisplay(this.activePage);
            deleteSub.unsubscribe();
          },
          (err) => {
            console.log('err');
            deleteSub.unsubscribe();
          }
        );
      }
      dialogSubscribe.unsubscribe();
    });


  }

}
