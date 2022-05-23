import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { CollectivePagesService } from '../../service/collective-pages.service';

import { CollectivePageListComponent } from './collective-page-list.component';

describe('CollectivePageListComponent', () => {
  let component: CollectivePageListComponent;
  let fixture: ComponentFixture<CollectivePageListComponent>;
  let testBedService: CollectivePagesService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CollectivePageListComponent ],
      imports:[HttpClientTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CollectivePageListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(CollectivePagesService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });



});
