import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent implements OnInit {

  dropdown:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }
  clickDropdown(){
    this.dropdown = !this.dropdown;
  }

  resetDropdown(){
    this.dropdown = false;
  }
}
