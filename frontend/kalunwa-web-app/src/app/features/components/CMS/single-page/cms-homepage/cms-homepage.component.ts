import { Component, OnInit } from '@angular/core';
import { EventsModel } from 'src/app/features/models/events';
import { HomepageService } from 'src/app/features/service/homepage.service';
import { HomeNewsModel } from 'src/app/features/models/home-news';
import { SinglePageListModel } from 'src/app/features/models/CMS/single-page-list-model';
import { ProjectItemService } from '../../../projects/service/project-item.service';
import { EventspageService } from 'src/app/features/service/eventspage.service';
import { NewsService } from '../../../news/service/news.service';

@Component({
  selector: 'app-cms-homepage',
  templateUrl: './cms-homepage.component.html',
  styleUrls: ['./cms-homepage.component.scss']
})
export class CmsHomepageComponent implements OnInit {

  constructor(private projectService: ProjectItemService, private eventsService: EventspageService, private newsService: NewsService) { }

  public jumbotron = [] as EventsModel[];
  public events = [] as EventsModel[];
  public projects = [] as EventsModel[];
  public news =[] as HomeNewsModel[];

  sectionChoice: string = 'jumbotron';

  details: SinglePageListModel={
    id: 1,
    page: "Homepage",
    status: "Published",
    updated_by: "Admin 1",
    last_updated: "12/11/21",
  }

  ngOnInit(): void {
    //---for jumbotron
    this.eventsService.getEventList()
      .subscribe(data => this.jumbotron = data);

    this.projectService.getProjectList()
      .subscribe(data => this.jumbotron = this.jumbotron.concat(data));
    //---for events
    this.eventsService.getEventList()
    .subscribe(data => this.events = data);
    //---for projects
    this.projectService.getProjectList()
      .subscribe(data => this.projects = data);
    //---for news
    this.newsService.getNewsList()
    .subscribe(data => this.news = data);
  }

  toggleSection(section:string){
    this.sectionChoice = section;
  }

  reset(id:string) {
    var dropDown = document.getElementById(id) as HTMLSelectElement;
    dropDown.selectedIndex = 0;
}

}
