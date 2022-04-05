import { Component, Inject, OnInit } from '@angular/core';
import { MembersDialogModel } from '../../models/members-dialog-model';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-members-dialog',
  templateUrl: './members-dialog.component.html',
  styleUrls: ['./members-dialog.component.scss']
})
export class MembersDialogComponent implements OnInit {

  constructor(@Inject(MAT_DIALOG_DATA) private data:number,
              private matDialogRef:MatDialogRef<MembersDialogComponent>) { }
  
  members: MembersDialogModel[]=[
    {
      id: 1,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Camp Leader",
    },
    {
      id: 2,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
    {
      id: 3,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
    {
      id: 4,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
    {
      id: 5,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
    {
      id: 6,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
    {
      id: 7,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
    {
      id: 8,
      member_img: "assets/images/person-icon.jpg",
      name: "Member Name",
      position:"Cabin Leader",
    },
  ];

  ngOnInit(): void {
  }

  ngOnDestroy(){
    this.matDialogRef.close();
  }

  getLimit(){
    return this.data
  }

}
