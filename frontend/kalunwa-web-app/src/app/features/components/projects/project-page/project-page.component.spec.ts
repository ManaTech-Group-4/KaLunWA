import { HttpClientTestingModule } from '@angular/common/http/testing';
import { async, ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { MatDialogModule } from '@angular/material/dialog';
import { ProjectItemsModel } from 'src/app/features/models/project-items-model';
import { ProjectItemService } from '../service/project-item.service';

import { ProjectPageComponent } from './project-page.component';

describe('ProjectPageComponent', () => {
  let component: ProjectPageComponent;
  let fixture: ComponentFixture<ProjectPageComponent>;
  let testBedService: ProjectItemService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProjectPageComponent ],
      providers: [ProjectItemService],
      imports : [MatDialogModule, HttpClientTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectPageComponent);
    testBedService = TestBed.get(ProjectItemService);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('Service injected via inject() and TestBed.get() should be the same instance (HomepageService)',
    inject([ProjectItemService], (injectService: ProjectItemService) => {
      expect(injectService).toBe(testBedService);
  }));

  it("should call openDialog and get the list of events according to fiter", async(() => {
    const response: ProjectItemsModel[] = [];

    spyOn(component, 'openDialog');

    component.openDialog();

    fixture.detectChanges();
    let result= [] as ProjectItemsModel[];
    component.projectDisplay$.subscribe(projects =>{result = projects;
    })
    expect(result).toEqual(response);
  }));
});
