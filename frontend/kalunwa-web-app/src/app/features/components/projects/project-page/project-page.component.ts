import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import { FilterProjectsDialogComponent } from 'src/app/features/dialog/filter-projects-dialog/filter-projects-dialog.component';

@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.scss']
})
export class ProjectPageComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  selectedCamps = [] as string[];
  selectedStatus = '';

  ngOnInit(): void {
  }
  openDialog() {
    const dialogRef = this.dialog.open(FilterProjectsDialogComponent);
    const subscribeDialog = dialogRef.componentInstance.applyFilter.subscribe((data:any) => {
      console.log('dialog data', data);
      this.selectedCamps = data.camps;
      this.selectedStatus = data.status;
    });

    dialogRef.afterClosed().subscribe(result => {
      subscribeDialog.unsubscribe();
    });
  }

}
