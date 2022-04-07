import { Component, OnInit } from '@angular/core';
import { ProjectItemsModel } from 'src/app/features/models/project-items-model';
import { ProjectItemService } from '../service/project-item.service';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.scss']
})
export class ProjectListComponent implements OnInit {

  constructor(private projectService: ProjectItemService) { }

  projectList = [] as ProjectItemsModel[];
  ngOnInit(): void {
    this.projectService.getProjectList()
      .subscribe(data => {
        this.projectList = data.map((project) =>({
          id: project.id,
          title: project.title,
          description: project.description,
          image: project.image.image,
          start_date: project.start_date,
          end_date: project.end_date,
          tags: [project.camp, project.status]
        }));
      });
  }

}
