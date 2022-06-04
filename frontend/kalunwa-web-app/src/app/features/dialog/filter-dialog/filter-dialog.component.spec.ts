import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatDialog, MatDialogModule, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FilterDialogComponent } from './filter-dialog.component';

describe('FilterDialogComponent', () => {
  let component: FilterDialogComponent;
  let fixture: ComponentFixture<FilterDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FilterDialogComponent ],
      imports : [ MatDialogModule, ReactiveFormsModule, FormsModule, BrowserAnimationsModule],
      providers: [
        { provide: MAT_DIALOG_DATA, useValue: {} }]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FilterDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('emit filter values', () => {
    spyOn(component.applyFilter, 'emit');
    component.clickFilter(['GNRL'],'sadf');

    fixture.detectChanges();
    expect(component.applyFilter.emit).toHaveBeenCalledWith({camps:['GNRL'],status:'sadf'});
  });


  it('reset values in statusControl', () => {
    spyOn(component.statusControl, 'reset');
    component.onStatusRemoved();

    fixture.detectChanges();
    expect(component.statusControl.reset).toHaveBeenCalled();
  });

  it('sucessfully remove a camp in the selectedCamps', () => {
    const mockArray = ['alpha', 'beta', 'charlie'];
    const mockResult = ['beta', 'charlie'];
    component.campControl.setValue(mockArray);

    component.onCatRemoved('alpha');
    expect(component.campControl.value as string[]).toEqual(mockResult);
  });

  it('sucessfully remove an element in the array', () => {
    const mockArray = ['alpha', 'beta', 'charlie'];
    const mockResult = ['beta', 'charlie'];
    component.removeFirst(mockArray, 'alpha');
    expect(mockResult).toEqual(mockArray);
  });

  it('input a non-existent element', () => {
    const mockArray = ['alpha', 'beta', 'charlie'];
    const mockResult = ['alpha', 'beta', 'charlie'];
    component.removeFirst(mockArray, 'asdfas');
    expect(mockResult).toEqual(mockArray);
  });

});
