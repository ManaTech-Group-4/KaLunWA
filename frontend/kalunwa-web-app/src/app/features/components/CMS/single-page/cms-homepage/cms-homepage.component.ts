import { Component, OnInit } from '@angular/core';
import { EventsModel } from 'src/app/features/models/events';
import { HomepageService } from 'src/app/features/service/homepage.service';
import { SinglePageListModel } from 'src/app/features/models/CMS/single-page-list-model';

@Component({
  selector: 'app-cms-homepage',
  templateUrl: './cms-homepage.component.html',
  styleUrls: ['./cms-homepage.component.scss']
})
export class CmsHomepageComponent implements OnInit {

  constructor(private homeService: HomepageService) { }

  public jumbotron = [] as EventsModel[];
  public events = [] as EventsModel[];
  public projects = [] as EventsModel[];

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
    this.homeService.getEvents()
      .subscribe(data => this.jumbotron = data);

    this.homeService.getProjects()
      .subscribe(data => this.jumbotron = this.jumbotron.concat(data));
    //---for events
    this.homeService.getEvents()
    .subscribe(data => this.events = data);
    //---for projects
    this.homeService.getProjects()
      .subscribe(data => this.projects = data);
  }

  toggleSection(section:string){
    this.sectionChoice = section;
  }

  reset(id:string) {
    var dropDown = document.getElementById(id) as HTMLSelectElement;
    dropDown.selectedIndex = 0;
}

}
