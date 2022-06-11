import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { AuthService } from 'src/app/admin/service/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  @Output() toggleSidebarEvent: EventEmitter<any> = new EventEmitter();
  admin_name = "";
  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.admin_name = this.authService.adminName;
  }

  toggleSidebar(){
    this.toggleSidebarEvent.emit();
  }
}
