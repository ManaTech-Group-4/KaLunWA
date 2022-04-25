import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EventsResponseModel } from '../models/events-response-model';

@Injectable({
  providedIn: 'root'
})
export class EventspageService {

  constructor(private http:HttpClient) { }

  getEventList() : Observable<EventsResponseModel[]>{
    return this.http.get<EventsResponseModel[]>('http://127.0.0.1:8000/api/events');

  }

}
