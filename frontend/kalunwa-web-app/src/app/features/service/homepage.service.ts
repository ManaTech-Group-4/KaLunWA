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


  featuredNews: HomeNewsModel[] = [
    { title: "News Headline 1",
      img: "assets/images/news/news1.jpg",
      date: "March 11, 2022",
      shortDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip..."},
    { title: "2nd Headline in News",
      img: "assets/images/news/new2.jpeg",
      date: "March 10, 2022",
      shortDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip..."},
    { title: "Headline of News 3",
      img: "assets/images/news/new3.jpg",
      date: "March 10, 2022",
      shortDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip..."}
  ];

  constructor(private http:HttpClient) { }


  public getEvents(): Observable<EventsModel[]>{
    return this.http.get<EventsModel[]>('http://127.0.0.1:8000/api/homepage/events');
  }

  public getProjects(): Observable<EventsModel[]> {
    return this.http.get<EventsModel[]>('http://127.0.0.1:8000/api/homepage/projects');
  }

  public getNews(): HomeNewsModel[] {
    return this.featuredNews;
  }

  public getJumbotron():Observable<JumbotronModel[]> {
    return this.http.get<JumbotronModel[]>('http://127.0.0.1:8000/api/homepage/jumbotrons');
  }

}
