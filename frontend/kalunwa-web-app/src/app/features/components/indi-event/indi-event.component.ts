import { getLocaleCurrencyCode } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { IndivEventsModel } from '../../models/indiv-event-model';
import { EventspageService } from '../../service/eventspage.service';

@Component({
  selector: 'app-indi-event',
  templateUrl: './indi-event.component.html',
  styleUrls: ['./indi-event.component.scss']
})
export class IndiEventComponent implements OnInit {


  event$: Observable<IndivEventsModel>;

  constructor(private route: ActivatedRoute, private eventService: EventspageService) { }


  ngOnInit(): void {

    const eventId = this.route.snapshot.paramMap.get("id");
    this.event$ = this.eventService.getEventDetails(eventId)
      .pipe(map((event: IndivEventsModel) => ({
        id: event.id,
        title: event.title,
        image: event.image,
        description: event.description,
        start_date: event.start_date,
        end_date: event.end_date,
        camp: event.camp,
        status: event.status,
        gallery: event.gallery
          .map(imageSlide =>
            ({image: imageSlide.image,
              thumbImage: imageSlide.image,
              id: imageSlide.id
            })
          ),
        contributors: event.contributors
      })
    ));
    this.event$.subscribe(event => console.log(event));
  }
}
