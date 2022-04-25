import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog'
import { Observable } from 'rxjs';;
import { map } from 'rxjs/operators';
import { FilterProjectsDialogComponent } from 'src/app/features/dialog/filter-projects-dialog/filter-projects-dialog.component';
import { ProjectItemsModel } from 'src/app/features/models/project-items-model';
import { ProjectResponseModel } from 'src/app/features/models/project-response-model';
import { ProjectItemService } from '../service/project-item.service';

@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.scss']
})
export class ProjectPageComponent implements OnInit {

  constructor(public dialog: MatDialog, private projectService:ProjectItemService) { }

  projectList$! : Observable<ProjectItemsModel[]>;
  projectDisplay$! : Observable<ProjectItemsModel[]>;

  ngOnInit(): void {
    this.projectList$ = this.projectService.getProjectList()
    .pipe(
      map((data: ProjectResponseModel[]) =>  data.map(project =>({
        id: project.id,
        title: project.title,
        description: project.description,
        image: project.image.image,
        start_date: project.start_date,
        end_date: project.end_date,
        tags: [project.camp, project.status]
      }))
      ));

    this.projectDisplay$ = this.projectList$;
  }
  openDialog() {
    const dialogRef = this.dialog.open(FilterProjectsDialogComponent);
    const subscribeDialog = dialogRef.componentInstance.applyFilter.subscribe((data:any) => {
      this.projectDisplay$ = this.projectList$.pipe(
        map(projects => projects
          .filter(
            project => data.camps.every((tag: string) => project.tags.includes(tag)) &&
              (data.status == '' || project.tags.includes(data.status))
          )
        )
      );
    });

    dialogRef.afterClosed().subscribe(result => {
      subscribeDialog.unsubscribe();
    });
  }

}
