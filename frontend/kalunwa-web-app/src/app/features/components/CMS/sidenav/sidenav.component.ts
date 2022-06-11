import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/admin/service/auth.service';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {

  dropdown:boolean = false;
  constructor(private authenticationService: AuthService,
    private router: Router) { }

  ngOnInit(): void {
  }
  clickDropdown(){
    this.dropdown = !this.dropdown;
  }

  resetDropdown(){
    this.dropdown = false;
  }
  logout() {
      this.authenticationService.logout().subscribe();
      this.router.navigate(['/login']);
  }
}
