import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.scss']
})
export class NavBarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  menu:boolean = false;
  displayMenu:string = "flex";

  onMenuClick(){
    if(this.menu == false){
      this.displayMenu = "flex";
      this.menu = !this.menu;
    }
    else{
      this.displayMenu = "none";
      this.menu = !this.menu;
    }
  }

}
