import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-org-structure',
  templateUrl: './org-structure.component.html',
  styleUrls: ['./org-structure.component.scss']
})
export class OrgStructureComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  showBaybayon:boolean=false
  showLasang:boolean=false
  showSuba:boolean=false
  showZW:boolean=false
  showBoT:boolean=false

  clickBaybayon(){
    this.showBaybayon=!this.showBaybayon

    if((this.showLasang=true) && (this.showSuba=true) && (this.showZW=true)){
      this.showLasang=!this.showLasang
      this.showSuba=!this.showSuba
      this.showZW=!this.showZW
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT
    }
  }
  clickLasang(){
    this.showLasang=!this.showLasang
    
    if((this.showBaybayon=true) && (this.showSuba=true) && (this.showZW=true)){
      this.showBaybayon=!this.showBaybayon
      this.showSuba=!this.showSuba
      this.showZW=!this.showZW
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT
    }
  }
  clickSuba(){
    this.showSuba=!this.showSuba
    
    if((this.showLasang=true) && (this.showBaybayon=true) && (this.showZW=true)){
      this.showLasang=!this.showLasang
      this.showBaybayon=!this.showBaybayon
      this.showZW=!this.showZW
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT
    }
  }
  clickZW(){
    this.showZW=!this.showZW
    
    if((this.showLasang=true) && (this.showSuba=true) && (this.showBaybayon=true)){
      this.showLasang=!this.showLasang
      this.showSuba=!this.showSuba
      this.showBaybayon=!this.showBaybayon
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT
    }
  }
  clickBoT(){
    this.showBoT=!this.showBoT
  }
}
