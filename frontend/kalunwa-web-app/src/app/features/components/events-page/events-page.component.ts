import { EventListenerFocusTrapInertStrategy } from '@angular/cdk/a11y';
import { Component, OnInit } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';
import { EventsItemsModel } from '../../models/events-items-model';
import { EventspageService } from '../../service/eventspage.service';

@Component({
  selector: 'app-events-page',
  templateUrl: './events-page.component.html',
  styleUrls: ['./events-page.component.scss']
})
export class EventsPageComponent implements OnInit {

  constructor( private eventsService: EventspageService) { }

  eventsList = [] as EventsItemsModel[];

  ngOnInit(): void {
    // this.eventsService.getEventList()
    //   .subscribe(data => this.eventsList = data);

  }

}
