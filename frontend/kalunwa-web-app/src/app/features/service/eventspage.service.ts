import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EventsItemsModel } from '../models/events-items-model';

@Injectable({
  providedIn: 'root'
})
export class EventspageService {

  constructor(private http:HttpClient) { }

  public getEventList() : Observable<EventsItemsModel[]>{
    return this.http.get<EventsItemsModel[]>('http://127.0.0.1:8000/api/events');
  }
}
