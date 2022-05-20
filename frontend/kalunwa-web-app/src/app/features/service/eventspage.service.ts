import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EventsResponseModel } from '../models/events-response-model';
import { IndivEventsModel } from '../models/indiv-event-model';

@Injectable({
  providedIn: 'root'
})
export class EventspageService {

  constructor(private http:HttpClient) { }

  getEventList() : Observable<EventsResponseModel[]>{
    return this.http.get<EventsResponseModel[]>('http://127.0.0.1:8000/api/events/?expand=image');

  }

  getEventDetails(eventId: string | null) : Observable<IndivEventsModel>{
    let address  = 'http://127.0.0.1:8000/api/events/'+eventId+'/?expand=image,contributors.image,gallery&omit=created_at,updated_at&query_limit_gallery=10';
    return this.http.get<IndivEventsModel>(address);
  }

}
