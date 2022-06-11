import { AfterViewInit, ChangeDetectorRef, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Observable, of } from 'rxjs';
import { EventsItemsModel } from '../../models/event-items-model';
import { EventspageService } from '../../service/eventspage.service';

@Component({
  selector: 'app-event-page-list',
  templateUrl: './event-page-list.component.html',
  styleUrls: ['./event-page-list.component.scss']
})
export class EventPageListComponent implements OnInit {

  @Input()
  events = [] as EventsItemsModel[];
  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 4;
  height:number;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    console.log(newPage,this.activePage);
    this.currentPage += (5*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 5;
    if(this.lastPage > this.events.length)
      this.lastPage = this.events.length;

    this.ref.detectChanges();
    this.activePage = newPage;
  }


  ngOnInit(): void {
  }


}
