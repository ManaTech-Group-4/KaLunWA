import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import { FilterDialogComponent } from '../../dialog/filter-dialog/filter-dialog.component';
import { TagModel } from '../../models/tags-model';

@Component({
  selector: 'app-events-page',
  templateUrl: './events-page.component.html',
  styleUrls: ['./events-page.component.scss']
})
export class EventsPageComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  selectedStatus = 'Upcoming' ;
  selectedCamp = ['Lasang','Baybayon'] as string[];

  ngOnInit(): void {

  }
  openDialog(camps: string[], status: string) {
    const dialogRef = this.dialog.open(FilterDialogComponent, {
      data: {dialogCamps: camps, dialogStatus: status}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  filterEvents(results: {camps:string[], status: string}){
    console.log("Results: " + results.status);
  }

}
