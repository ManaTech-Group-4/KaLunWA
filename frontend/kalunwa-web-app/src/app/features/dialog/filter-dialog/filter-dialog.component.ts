import { Component, EventEmitter, Inject, OnInit, Output} from '@angular/core';
import {FormControl} from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import { TagModel } from '../../models/tags-model';


@Component({
  selector: 'app-filter-dialog',
  templateUrl: './filter-dialog.component.html',
  styleUrls: ['./filter-dialog.component.scss']
})
export class FilterDialogComponent implements OnInit {

  constructor() { }

  allCamps: {[camp_name: string]: string;} = {
    'General': '#121212',
    'Baybayon':'#D9B863',
    'Lasang':'#3F6218',
    'Suba':'#1C8BD4',
    'Zero Waste':'#9CCC65',
  };

  allStatus: {[status_name: string]: string;} = {
    'Upcoming': '#f44336',
    'Past':'#C4C4C4'
  };


  @Output() applyFilter = new EventEmitter<{camps:string[], status: string}>();


  campControl = new FormControl([]);
  statusControl = new FormControl([]);

  clickFilter(camps:any, status:string){
    this.applyFilter.emit({camps: camps, status: status});
  }

  onCatRemoved(cat: string) {
    const camp = this.campControl.value as string[];
    this.removeFirst(camp, cat);
    this.campControl.setValue(camp); // To trigger change detection


  }

  onStatusRemoved() {
    this.statusControl.reset()// To trigger change detection


  }


  removeFirst(array: string[], toRemove: string): void {

    const index = array.indexOf(toRemove);
    if (index !== -1) {
      array.splice(index, 1);
    }
  }

  ngOnInit(): void {
  }
}
