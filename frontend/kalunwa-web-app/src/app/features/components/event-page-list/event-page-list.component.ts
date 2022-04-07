import { Component, OnInit } from '@angular/core';
import { EventsItemsModel } from '../../models/event-items-model';
import { EventspageService } from '../../service/eventspage.service';

@Component({
  selector: 'app-event-page-list',
  templateUrl: './event-page-list.component.html',
  styleUrls: ['./event-page-list.component.scss']
})
export class EventPageListComponent implements OnInit {

  constructor( private eventsService: EventspageService) { }

  eventsList = [] as EventsItemsModel[];
  ngOnInit(): void {
    this.eventsService.getEventList()
      .subscribe(data => {
        this.eventsList = data.map((event) =>({
          id: event.id,
          title: event.title,
          description: event.description,
          image: event.image.image,
          start_date: event.start_date,
          end_date: event.end_date,
          tags: [event.camp, event.status]
        }));
      });
  }

}
