import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
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
  constructor() { }




  ngOnInit(): void {
  }


}
