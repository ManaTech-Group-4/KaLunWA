import { Component, OnInit } from '@angular/core';
import { EventsModel } from './../../models/events';
import { HomepageService } from './../../service/homepage.service';
import { HomeCampModel } from './../../models/home-camp';
import { HomeNewsModel } from './../../models/home-news';
import { map, subscribeOn } from 'rxjs/operators';
import { homepageInfo } from '../../models/homepage-container-model';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {


  constructor(private homeService: HomepageService) { }


  whatWeDo : boolean = false
  about: boolean = false;
  orgOverview : boolean = false;

  public events = [] as homepageInfo.PageContainedEvent[];
  public projects = [] as homepageInfo.PageContainedProject[];
  public jumbotron = [] as homepageInfo.PageContainedJumbotron[];
  public news =[] as HomeNewsModel[];
  public camps : HomeCampModel[] = [
    {
      title:"Baybayon",
      img: "assets/images/baybayon.png",
      color: "#ECDBB2",
      link: "/baybayon",
    },
    {
      title:"Lasang",
      img: "assets/images/lasang.png",
      color: "#3F6218",
      link: "/lasang",
    },
    {
      title:"Suba",
      img: "assets/images/suba.png",
      color: "#1C8BD4",
      link: "/suba",
    },
    {
      title:"Zero Waste",
      img: "assets/images/zero.png",
      color: "#9CCC65",
      link: "/zero-waste",
    },
  ];

  ngOnInit(): void {
    // this.homeService.getHomepage()
    //   .subscribe((data: HomepageContainer) => {
    //     this.events = data.page_contained_events;
    //     this.projects = data.page_contained_projects;
    //     console.log(this.events);
    //     console.log(this.projects);
    //   });


    this.homeService.getHomepage().subscribe((data: homepageInfo.HomepageContainer) => {
        this.events = data.page_contained_events;
        this.projects = data.page_contained_projects;
        this.jumbotron = data.page_contained_jumbotrons;
      });

    this.homeService.getNews()
    .subscribe(data => this.news = data);
  }


}
