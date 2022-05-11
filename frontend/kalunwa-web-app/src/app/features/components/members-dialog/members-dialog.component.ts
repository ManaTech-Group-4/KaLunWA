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
      quote: "I just wanna tell you how I'm feeling",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 2,
      member_img: "assets/images/person-icon.jpg",
      quote: "Gotta make you understand",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 3,
      member_img: "assets/images/person-icon.jpg",
      quote: "Never gonna give you up",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 4,
      member_img: "assets/images/person-icon.jpg",
      quote: "Never gonna let you down",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 5,
      member_img: "assets/images/person-icon.jpg",
      quote: "Never gonna run around and desert you",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 6,
      member_img: "assets/images/person-icon.jpg",
      quote: "Never gonna make you cry",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 7,
      member_img: "assets/images/person-icon.jpg",
      quote: "Never gonna say goodbye",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
    {
      id: 8,
      member_img: "assets/images/person-icon.jpg",
      quote: "Never gonna tell a lie and hurt you",
      first_name: "Member Name",
      last_name: "ASdfasfd",
      position:"Position",
    },
  ];

  ngOnInit(): void {
  }

  close(){
    this.matDialogRef.close();
  }

  getLimit(){
    return this.data
  }

}
