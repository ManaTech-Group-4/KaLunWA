import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ProfileReceive } from 'src/app/admin/model/user-model';
import { AuthService } from 'src/app/admin/service/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  @Output() toggleSidebarEvent: EventEmitter<any> = new EventEmitter();
  admin_name = "";
  adminImage:any;
  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    const currentAdminSub = this.authService.currentAdmin.subscribe(
      (res: ProfileReceive)=>{
        this.admin_name = res.username;
        this.adminImage = res.image
        currentAdminSub.unsubscribe();
      }
    );
  }

  toggleSidebar(){
    this.toggleSidebarEvent.emit();
  }
}
