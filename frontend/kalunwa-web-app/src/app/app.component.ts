import { Component, OnInit } from '@angular/core';
import { EventsModel } from './features/models/events';
import { HomepageService } from './features/service/homepage.service';
import { HomeCampModel } from './features/models/home-camp';
import { HomeNewsModel } from './features/models/home-news';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'kalunwa-web-app';


  constructor(private homeService: HomepageService) { }


  whatWeDo : boolean = false
  about: boolean = false;
  orgOverview : boolean = false;

  public events = [] as EventsModel[];
  public projects = [] as EventsModel[];
  public news =[] as HomeNewsModel[];
  public camps : HomeCampModel[] = [
    {
      title:"Baybayon",
      img: "assets/images/baybayon.png",
      color: "#ECDBB2"
    },
    {
      title:"Lasang",
      img: "assets/images/lasang.png",
      color: "#3F6218"
    },
    {
      title:"Suba",
      img: "assets/images/suba.png",
      color: "#1C8BD4"
    },
    {
      title:"Zero Waste",
      img: "assets/images/zero.png",
      color: "#9CCC65"
    },
  ];

  ngOnInit(): void {
    this.getEventsDisplay();
    this.getProjectsDisplay();
    this.getNewsDisplay();
  }

  getEventsDisplay(): void {
    this.events = this.homeService.getEvents();
    console.log(this.events);
  }

  getProjectsDisplay(): void {
    this.projects = this.homeService.getProjects();
    console.log(this.projects);
  }

  getNewsDisplay(): void {
    this.news = this.homeService.getNews();
    console.log(this.news);
  }
}
