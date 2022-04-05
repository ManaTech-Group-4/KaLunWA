import { Component, Input, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MembersDialogComponent } from '../members-dialog/members-dialog.component';

@Component({
  selector: 'app-org-structure',
  templateUrl: './org-structure.component.html',
  styleUrls: ['./org-structure.component.scss']
})
export class OrgStructureComponent implements OnInit {

  constructor(private matDialog:MatDialog) { }

  ngOnInit(): void {
  }

  showBaybayon:boolean=false
  showLasang:boolean=false
  showSuba:boolean=false
  showZW:boolean=false
  showBoT:boolean=false

  clickBaybayon(){
    this.showBaybayon=!this.showBaybayon

    if((this.showLasang==true) && (this.showSuba==true) && (this.showZW==true)){
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
    
    if((this.showBaybayon==true) && (this.showSuba==true) && (this.showZW==true)){
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
    
    if((this.showLasang==true) && (this.showBaybayon==true) && (this.showZW==true)){
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
    
    if((this.showLasang==true) && (this.showSuba==true) && (this.showBaybayon==true)){
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

    if (this.showBaybayon==true){
      this.showBaybayon=!this.showBaybayon
    } else if (this.showLasang==true){
      this.showLasang=!this.showLasang
    } else if (this.showSuba==true){
      this.showSuba=!this.showSuba
    } else if(this.showZW==true){
      this.showZW=!this.showZW
    }
  }

  openDialog(members:number){
    this.matDialog.open(MembersDialogComponent,
      {
        data: members
      });

    
  }
}
