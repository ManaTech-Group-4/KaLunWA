import { ChangeDetectorRef, Component, Input, OnInit } from '@angular/core';
import { ProjectItemsModel } from 'src/app/features/models/project-items-model';
import { ProjectItemService } from '../service/project-item.service';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.scss']
})
export class ProjectListComponent implements OnInit {

  @Input()
  projects = [] as ProjectItemsModel[];
  constructor(private ref: ChangeDetectorRef) { }

  activePage:number = 1;
  currentPage = 0;
  lastPage = 4;

  detectIfChanges(){
    this.ref.detectChanges();
  }

  updateDisplay(newPage:number){
    console.log(newPage,this.activePage);
    this.currentPage += (5*(newPage-this.activePage));
    if(this.currentPage < 0)
      this.currentPage = 0;

    this.lastPage = this.currentPage + 5;
    if(this.lastPage > this.projects.length)
      this.lastPage = this.projects.length;

    this.ref.detectChanges();
    this.activePage = newPage;
  }


  ngOnInit(): void {
  }

}
