import { Component, OnInit } from '@angular/core';
<<<<<<< HEAD
=======
import { MatDialog } from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { MembersDialogModel } from '../../models/members-dialog-model';
import { OrgService } from '../../service/org.service';
import { MembersDialogComponent } from '../members-dialog/members-dialog.component';
>>>>>>> main

@Component({
  selector: 'app-org-structure',
  templateUrl: './org-structure.component.html',
  styleUrls: ['./org-structure.component.scss']
})
export class OrgStructureComponent implements OnInit {

<<<<<<< HEAD
  constructor() { }
=======
  constructor(private matDialog:MatDialog, private orgService: OrgService) { }
  execs$: Observable<MembersDialogModel[]>;
  directors$ :  Observable<MembersDialogModel[]>;
  campLeaders$: Observable<MembersDialogModel[]>;
  cabinOfficers$: Observable<MembersDialogModel[]>;
  grievance$: Observable<MembersDialogModel[]>;
  election$: Observable<MembersDialogModel[]>;
  selectedCamp: string = '';
>>>>>>> main

  ngOnInit(): void {
    this.execs$ = this.orgService.getExec().pipe(map(
      list => list.filter(member => member.position != 'Director')
    ));
    this.directors$ = this.orgService.getExec().pipe(map(
      list => list.filter(member => member.position == 'Director')
    ));
    this.cabinOfficers$ = this.orgService.getCabin();
    this.grievance$ = this.orgService.getGrievance();
    this.election$ = this.orgService.getElection();
  }

  showBaybayon:boolean=false;
  showLasang:boolean=false;
  showSuba:boolean=false;
  showZW:boolean=false;
  showBoT:boolean=false;

  clickBaybayon(){
    this.showBaybayon=!this.showBaybayon;

<<<<<<< HEAD
    if((this.showLasang=true) && (this.showSuba=true) && (this.showZW=true)){
      this.showLasang=!this.showLasang;
      this.showSuba=!this.showSuba;
      this.showZW=!this.showZW;
=======
    if(this.showBaybayon == true){
      this.selectedCamp = "Baybayon";
      this.campLeaders$ = this.orgService.getCampLeaders(this.selectedCamp);
    }
    else
      this.selectedCamp = '';

    if (this.showLasang){
      this.showLasang=!this.showLasang
    }

    if (this.showSuba){
      this.showSuba=!this.showSuba
    }

    if (this.showZW){
      this.showZW=!this.showZW
>>>>>>> main
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT;
    }
  }
  clickLasang(){
    this.showLasang=!this.showLasang;
<<<<<<< HEAD
=======

    if(this.showLasang == true){
      this.selectedCamp = "Lasang";
      this.campLeaders$ = this.orgService.getCampLeaders(this.selectedCamp);
    }
    else
      this.selectedCamp = '';


    if (this.showBaybayon){
      this.showBaybayon=!this.showBaybayon
    }
>>>>>>> main

    if((this.showBaybayon=true) && (this.showSuba=true) && (this.showZW=true)){
      this.showBaybayon=!this.showBaybayon;
      this.showSuba=!this.showSuba;
      this.showZW=!this.showZW;
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT;
    }
  }
  clickSuba(){
    this.showSuba=!this.showSuba;
<<<<<<< HEAD
=======

    if(this.showSuba == true){
      this.selectedCamp = "Suba";
      this.campLeaders$ = this.orgService.getCampLeaders(this.selectedCamp);
    }
    else
      this.selectedCamp = '';

    if (this.showBaybayon){
      this.showBaybayon=!this.showBaybayon
    }

    if (this.showLasang){
      this.showLasang=!this.showLasang
    }
>>>>>>> main

    if((this.showLasang=true) && (this.showBaybayon=true) && (this.showZW=true)){
      this.showLasang=!this.showLasang;
      this.showBaybayon=!this.showBaybayon;
      this.showZW=!this.showZW;
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT;
    }
  }
  clickZW(){
    this.showZW=!this.showZW;
<<<<<<< HEAD
=======

    if(this.showZW == true){
      this.selectedCamp = "Zero Waste";
      this.campLeaders$ = this.orgService.getCampLeaders(this.selectedCamp);
    }
    else
      this.selectedCamp = '';

    if (this.showBaybayon){
      this.showBaybayon=!this.showBaybayon
    }
>>>>>>> main

    if((this.showLasang=true) && (this.showSuba=true) && (this.showBaybayon=true)){
      this.showLasang=!this.showLasang;
      this.showSuba=!this.showSuba;
      this.showBaybayon=!this.showBaybayon;
    }

    if (this.showBoT){
      this.showBoT=!this.showBoT;
    }
  }
  clickBoT(){
    this.showBoT=!this.showBoT;
<<<<<<< HEAD
=======
    this.selectedCamp = '';

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

  getLeadersList(filter: string, members: Observable<MembersDialogModel[]>){
    if(filter != ''){
      members = members.pipe(map(
        list => list.filter(member => member.position == filter)
      ));
    }

    this.openDialog(members);
  }

  openDialog(members:Observable<MembersDialogModel[]>){
    this.matDialog.open(MembersDialogComponent,
    {
      data: members
    });


>>>>>>> main
  }
}
