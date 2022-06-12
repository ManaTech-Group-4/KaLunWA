import { Component, OnInit } from '@angular/core';
import { EventsModel } from 'src/app/features/models/events';
import { HomepageService } from 'src/app/features/service/homepage.service';
import { NewsService } from '../../../news/service/news.service';
import { HomeNewsModel } from 'src/app/features/models/home-news';
import { SinglePageListModel } from 'src/app/features/models/CMS/single-page-list-model';
import { JumbotronModel } from 'src/app/features/models/slides-model';
import { EventspageService } from 'src/app/features/service/eventspage.service';
import { ProjectItemService } from '../../../projects/service/project-item.service';
import { EventsResponseModel } from 'src/app/features/models/events-response-model';
import { ProjectResponseModel } from 'src/app/features/models/project-response-model';
import {FormGroup,FormControl} from '@angular/forms'
@Component({
  selector: 'app-cms-homepage',
  templateUrl: './cms-homepage.component.html',
  styleUrls: ['./cms-homepage.component.scss']
})
export class CmsHomepageComponent implements OnInit {
  constructor(private projectService: ProjectItemService, private eventsService: EventspageService) { }

  public jumbotron = [] as EventsResponseModel[];
  public events = [] as EventsResponseModel[];
  public projects = [] as EventsResponseModel[];

  sectionChoice: string = 'jumbotron';
  slides: number = 1;

  chosen: Array<any>=[
    0
  ];

  log(value:any){
    this.chosen.push(value);
    console.log(this.chosen);

  }
  onChange(index:number, value:any) {   
    this.chosen[index]=this.jumbotron.filter(x=>x.id!=value)
  }

  slide1=new FormGroup({
    id:new FormControl(null)
  })
  slide2=new FormGroup({
    id:new FormControl(null)
  })
  slide3=new FormGroup({
    id:new FormControl(null)
  })
  form=new FormGroup({
    id:new FormControl(null)
  })

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
  }

  toggleSection(section:string){
    this.sectionChoice = section;
  }

  reset(id:string) {
    var dropDown = document.getElementById(id) as HTMLSelectElement;
    dropDown.selectedIndex = 0;
  }

  addSlide(){
    this.slides++;
  }

  deleteSlide(){
    if (this.slides>1){
      this.slides--;
    }
    else{
      alert("Minimum of 1 slide needed");
    }
  }

}
