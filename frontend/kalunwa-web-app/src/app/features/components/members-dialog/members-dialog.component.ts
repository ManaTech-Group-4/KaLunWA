import { Component, Inject, Input, OnInit } from '@angular/core';
import { MembersDialogModel } from '../../models/members-dialog-model';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { OrgService } from '../../service/org.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-members-dialog',
  templateUrl: './members-dialog.component.html',
  styleUrls: ['./members-dialog.component.scss']
})
export class MembersDialogComponent implements OnInit {


  constructor(@Inject(MAT_DIALOG_DATA) public members$: Observable<MembersDialogModel[]>,
              private matDialogRef:MatDialogRef<MembersDialogComponent>,
              private service: OrgService) { }


  ngOnInit(): void {
  }

  close(){
    this.matDialogRef.close();
  }


}
