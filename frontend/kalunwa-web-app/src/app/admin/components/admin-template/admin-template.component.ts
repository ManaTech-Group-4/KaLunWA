import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin-template',
  templateUrl: './admin-template.component.html',
  styleUrls: ['./admin-template.component.scss']
})
export class AdminTemplateComponent implements OnInit {

  constructor() { }
  sidebarOpen:boolean=true;

  ngOnInit(): void {
  }
  sidebarToggle(){
    this.sidebarOpen = !this.sidebarOpen;
  }

}
