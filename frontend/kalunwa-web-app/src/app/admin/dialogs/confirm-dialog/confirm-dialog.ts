import { Component, EventEmitter, Inject, OnInit, Output } from "@angular/core";
import { MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";

@Component({
  selector: 'confirm-dialog',
  templateUrl: './confirm-dialog.html',
  styleUrls: ['./confirm-dialog.scss']
})

export class ConfirmDialog implements OnInit {
  header = "Delete User";


  @Output() submitClicked = new EventEmitter<boolean>();

  constructor(public dialogRef: MatDialogRef<ConfirmDialog>,
    @Inject(MAT_DIALOG_DATA) public data: string){}

  ngOnInit(): void {

  }

  confirm(response:boolean){
    this.dialogRef.close(response);
  }
}
