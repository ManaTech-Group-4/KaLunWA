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



  campList: TagModel[] = [
    {"name":'General',"color": '#121212'},
    {"name":'Baybayon',"color":'#D9B863'},
    {"name":'Lasang',"color":'#3F6218'},
    {"name":'Suba',"color":'#1C8BD4'},
    {"name":'Zero Waste',"color":'#9CCC65'}
  ];

  allStatus: {[status_name: string]: string;} = {
    'Upcoming': '#f44336',
    'Past':'#C4C4C4'
  };

  statusList: TagModel[] = [
    {"name":'Upcoming',"color": '#f44336'},
    {"name":'Past',"color": '#C4C4C4'},
  ];

  @Output() applyFilter = new EventEmitter<{camps:string[], status: string}>();



  filterForm: FormGroup = new FormGroup({});
  campControl = new FormControl([]);
  statusControl = new FormControl();
  initialCamps = [] as TagModel[];
  constructor(
    public dialogRef: MatDialogRef<FilterDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any, private fb: FormBuilder) {

      this.initialCamps = this.campList.filter(camp => this.data.dialogCamps.includes(camp.name));
      this.filterForm = fb.group({
        campControl: [this.initialCamps, [Validators.required]],
        statusControl: [this.statusList.filter(status => status.name == this.data.dialogStatus), [Validators.required]],
      });
      console.log(this.filterForm.value.statusControl);
    }


  clickFilter(camps:string[], status:string){
    console.log(this.filterForm.value.statusControl);
    console.log(this.filterForm.value.campControl);
    this.applyFilter.emit({camps, status});
    console.log("asdfasdf " + this.filterForm.value.campControl + " sdfasdf " + this.filterForm.value.statusControl)
  }

  get f(){
    return this.filterForm.controls;
  }

  removeCamp(camp: TagModel){
    let index = this.filterForm.value.campControl.indexOf(camp);
    this.filterForm.value.campControl.splice(index,1);
  }

  onStatusRemoved() {
    this.filterForm.value.statusControl.splice(0,1);
  }

  logIt(){
    console.log(this.filterForm.value.campControl);
  }

  ngOnInit(): void {
  }

}
