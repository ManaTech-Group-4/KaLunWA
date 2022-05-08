import { Component, Input, OnInit } from '@angular/core';
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

  constructor() { }

  ngOnInit(): void {

  }

}
