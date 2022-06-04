import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EventsModel } from '../models/events';
import { HomeNewsModel } from '../models/home-news';
import { JumbotronModel } from '../models/slides-model';


@Injectable({
  providedIn: 'root'
})
export class HomepageService {



  constructor(private http:HttpClient) { }


  public getEvents(): Observable<EventsModel[]>{
    return this.http.get<EventsModel[]>('http://127.0.0.1:8000/api/homepage/events');
  }

  public getProjects(): Observable<EventsModel[]> {
    return this.http.get<EventsModel[]>('http://127.0.0.1:8000/api/homepage/projects');
  }

  public getNews(): Observable<HomeNewsModel[]> {
    return this.http.get<HomeNewsModel[]>('http://127.0.0.1:8000/api/homepage/news');
  }

  public getJumbotron():Observable<JumbotronModel[]> {
    return this.http.get<JumbotronModel[]>('http://127.0.0.1:8000/api/jumbotrons/?expand=image&omit=created_at,updated_at,image.id&query_limit=5');
  }

}
