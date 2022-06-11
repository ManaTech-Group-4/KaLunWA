import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EventsModel } from '../models/events';
import { HomeNewsModel } from '../models/home-news';
import { homepageInfo } from '../models/homepage-container-model';
import { JumbotronModel } from '../models/slides-model';


@Injectable({
  providedIn: 'root'
})
export class HomepageService {



  constructor(private http:HttpClient) { }


  // public getEvents(): Observable<EventsModel[]>{
  //   return this.http.get<EventsModel[]>('http://127.0.0.1:8000/api/events/?expand=image&fields=id,title,image.image&is_featured=True&query_limit=3');
  // }

  // public getProjects(): Observable<EventsModel[]> {
  //   return this.http.get<EventsModel[]>('http://127.0.0.1:8000/api/projects/?expand=image&fields=id,title,image.image&is_featured=True&query_limit=3');
  // }

  public getNews(): Observable<HomeNewsModel[]> {
    return this.http.get<HomeNewsModel[]>('http://127.0.0.1:8000/api/news/?expand=image&omit=created_at,updated_at,image.id&query_limit=3');
  }

  public getHomepage():Observable<homepageInfo.HomepageContainer> {
    return this.http.get<homepageInfo.HomepageContainer>('http://127.0.0.1:8000/api/page-containers/homepage/?expand=page_contained_jumbotrons.jumbotron.image,page_contained_events.event.image,page_contained_projects.project.image');
  }

}
