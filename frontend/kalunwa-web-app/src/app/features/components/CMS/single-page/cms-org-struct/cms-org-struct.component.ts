import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { MembersDialogModel } from 'src/app/features/models/members-dialog-model';
import { OrgService } from 'src/app/features/service/org.service';

@Component({
  selector: 'app-cms-org-struct',
  templateUrl: './cms-org-struct.component.html',
  styleUrls: ['./cms-org-struct.component.scss']
})
export class CmsOrgStructComponent implements OnInit {

    constructor(private orgService: OrgService) { }
    execs$: Observable<MembersDialogModel[]>;
    directors$ :  Observable<MembersDialogModel[]>;
    campLeaders$: Observable<MembersDialogModel[]>;
    cabinOfficers$: Observable<MembersDialogModel[]>;
    grievance$: Observable<MembersDialogModel[]>;
    election$: Observable<MembersDialogModel[]>;
    selectedCamp: string = '';
    
    selectedComm:Observable<MembersDialogModel[]>;
    
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
      this.selectedComm = this.directors$;
    }
    
    toggleComm(filter:string){
      if(filter == 'Baybayon' || filter == 'Lasang' ||filter == 'Suba' ||filter == 'Zero Waste'){
        this.campLeaders$ = this.orgService.getCampLeaders(filter);
      }    
    }
    getLeadersList(filter: string, members: Observable<MembersDialogModel[]>){
      if(filter != ''){
        members = members.pipe(map(
          list => list.filter(member => member.position == filter)
        ));
      }

      this.selectedComm = members;
    }

}
