import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { FilterDialogComponent } from '../../dialog/filter-dialog/filter-dialog.component';
import { EventsItemsModel } from '../../models/event-items-model';
import { EventsResponseModel } from '../../models/events-response-model';
import { TagModel } from '../../models/tags-model';
import { EventspageService } from '../../service/eventspage.service';

@Component({
  selector: 'app-events-page',
  templateUrl: './events-page.component.html',
  styleUrls: ['./events-page.component.scss']
})
export class EventsPageComponent implements OnInit {

  constructor(public dialog: MatDialog, private eventService: EventspageService) { }

  eventList$! : Observable<EventsItemsModel[]>;
  eventDisplay$! : Observable<EventsItemsModel[]>;


  ngOnInit(): void {
    this.eventList$ = this.eventService.getEventList()
    .pipe(
      map((data: EventsResponseModel[]) =>  data.map(project =>({
        id: project.id,
        title: project.title,
        description: project.description,
        image: project.image.image,
        start_date: project.start_date,
        end_date: project.end_date,
        tags: [project.camp, project.status]
      }))
      ));

    this.eventDisplay$ = this.eventList$;
  }
  openDialog() {
    const dialogRef = this.dialog.open(FilterDialogComponent);
    const subscribeDialog = dialogRef.componentInstance.applyFilter.subscribe((data:any) => {
      this.eventDisplay$ = this.eventList$.pipe(
        map(event => event
          .filter(
            event => data.camps.every((tag: string) => event.tags.includes(tag)) &&
                        (data.status == '' || event.tags.includes(data.status))
          )
        )
      );
      this.eventDisplay$.subscribe(res => console.log(res));
      this.eventList$.pipe(
        map(event => event
          .filter(
            event => data.camps.every((tag: string) => event.tags.includes(tag))
          )
        )
      ).subscribe(res => console.log(res));
    });
    dialogRef.afterClosed().subscribe(result => {
      subscribeDialog.unsubscribe();
    });
  }
}
