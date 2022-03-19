import { Injectable } from '@angular/core';
import { EventsModel } from '../models/events';
import { HomeNewsModel } from '../models/home-news';


@Injectable({
  providedIn: 'root'
})
export class HomepageService {

  featuredEvents: EventsModel[] = [
    { title: "Event 1",
      img: "assets/images/event.jpg"},
    { title: "Event 2",
      img: "assets/images/event.jpg"},
    { title: "Event 3",
      img: "assets/images/event.jpg"}
  ];


  featuredProjects: EventsModel[] = [
    { title: "Projects 1",
      img: "assets/images/project.jpg"},
    { title: "Projects 2",
      img: "assets/images/project.jpg"},
    { title: "Projects 3",
      img: "assets/images/project.jpg"}
  ];

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

  constructor() { }


  public getEvents(): EventsModel[] {
    return this.featuredEvents;
  }

  public getProjects(): EventsModel[] {
    return this.featuredProjects;
  }

  public getNews(): HomeNewsModel[] {
    return this.featuredNews;
  }

}
