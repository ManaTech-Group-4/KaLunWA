import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CollectivePageListComponent } from './collective-page-list.component';

describe('CollectivePageListComponent', () => {
  let component: CollectivePageListComponent;
  let fixture: ComponentFixture<CollectivePageListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CollectivePageListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CollectivePageListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
