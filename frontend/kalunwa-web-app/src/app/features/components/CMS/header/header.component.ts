import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { AuthService } from 'src/app/admin/service/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  adminName:string;

  @Output() toggleSidebarEvent: EventEmitter<any> = new EventEmitter();
  constructor( private authService: AuthService) {
    this.adminName = authService.adminName;
  }

  ngOnInit(): void {
  }

  toggleSidebar(){
    this.toggleSidebarEvent.emit();
  }
}
